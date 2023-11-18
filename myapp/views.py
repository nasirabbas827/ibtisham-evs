from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm 
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages 
from .forms import CustomUserChangeForm


from django.shortcuts import render
from .models import Election, Candidate

def home(request):
    elections = Election.objects.all()
    candidates = Candidate.objects.all()
    context = {
        'elections': elections,
        'candidates': candidates,
    }
    return render(request, 'home.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Election, Candidate

def view_candidates(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    candidates = Candidate.objects.filter(election=election)
    context = {
        'election': election,
        'candidates': candidates,
    }
    return render(request, 'view_candidates.html', context)


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Election, Candidate, BlockchainRecord
from .blockchain import Blockchain
import json

blockchain = Blockchain()

@login_required
def cast_vote(request, election_id, candidate_id):
    election = get_object_or_404(Election, pk=election_id)
    candidate = get_object_or_404(Candidate, pk=candidate_id)

    # Check if the election is ongoing
    if election.status != 'ongoing':
        return HttpResponse("Voting is not allowed for this election. Election status: {}".format(election.status))

    # Check if the user has already cast a vote in this election
    existing_vote = BlockchainRecord.objects.filter(user=request.user, election=election).exists()
    if existing_vote:
        return HttpResponse("You have already cast a vote in this election.")

    # Add the vote to the blockchain
    blockchain.add_vote(voter=request.user.username, candidate=candidate.name)

    # Mine the block to generate blockchain hash
    block = blockchain.get_latest_block()

    # Save the blockchain to the database
    block_data = json.dumps(vars(block))
    block_hash = block.hash
    prev_hash = block.previous_hash
    BlockchainRecord.objects.create(user=request.user, election=election, candidate=candidate, block_data=block_data, block_hash=block_hash, prev_hash=prev_hash)

    # You can store the block_index or any other relevant information in your database
    # For simplicity, let's just return a success message
    return render(request, 'vote_cast_success.html', {'block_index': len(blockchain.chain)})




def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('home')

def custom_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})




@login_required
def update_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')  # Add a success message
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'update_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'change_password.html', {'form': form})


from django.shortcuts import render
from .models import Election, Candidate, BlockchainRecord

def view_results(request):
    # Retrieve completed elections
    completed_elections = Election.objects.filter(status='completed')

    # Dictionary to store election results
    election_results = {}

    for election in completed_elections:
        # Retrieve all candidates for the election
        candidates = Candidate.objects.filter(election=election)

        # Dictionary to store candidate votes
        candidate_votes = {}

        # Retrieve all blockchain records for the completed election
        blockchain_records = BlockchainRecord.objects.filter(election=election)

        # Initialize votes count for each candidate
        for candidate in candidates:
            candidate_votes[candidate.name] = 0

        # Count the votes for each candidate
        for record in blockchain_records:
            candidate_name = record.candidate.name
            candidate_votes[candidate_name] += 1

        # Store election results in the dictionary
        election_results[election] = candidate_votes

    context = {
        'election_results': election_results,
    }

    return render(request, 'view_results.html', context)
