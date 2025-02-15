from django.shortcuts import render, redirect, get_object_or_404

from .forms import ConversationMessageForm
from .models import ConversationModel, ConversationMessageModel
from django.contrib.auth.decorators import login_required


from item.models import Item

@login_required
def NewConversationView(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = ConversationModel.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = ConversationModel.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_massage = form.save(commit=False)
            conversation_massage.conversation = conversation
            conversation_massage.created_by = request.user
            conversation_massage.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    template_name = 'new.html'
    context = {
        'form': form
    }

    return render(request, template_name, context)


@login_required
def Inbox(request):
    conversations = ConversationModel.objects.filter(members__in=[request.user.id])

    template_name = 'inbox.html'
    context = {
        'conversations': conversations
    }

    return render(request, template_name, context)


@login_required
def detail(request, pk):
    conversation = ConversationModel.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()
            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()


    template_name = 'conversation_detail.html'
    context = {
        'conversation': conversation,
        'form': form
    }
    return render(request, template_name, context)
