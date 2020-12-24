from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'blog/topics.html', context)


def topic(request, topic_id):
    topic_db = Topic.objects.get(id=topic_id)
    entries = topic_db.entry_set.order_by('-date_added')
    context = {'topic': topic_db, 'entries': entries}
    return render(request, 'blog/topic.html', context)


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:topics'))
    context = {'form': form}
    return render(request, 'blog/new_topic.html', context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    print(topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            print(new_entry)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('blog:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    print('--------------------------------')
    return render(request, 'blog/new_entry.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'blog/edit_entry.html', context)
