from django.shortcuts import render, redirect
from django.http import HttpResponse
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Job
from django.contrib.messages import add_message
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, "track/index.html")


def job_profile(request):
    jobs = Job.objects.all()
    context = {"jobs": jobs}
    return render(request, "track/job_profile.html", context)


def view_profile(request, pk):
    job = Job.objects.get(id=pk)
    if request.method == 'POST':
        res = request.FILES['resume']
        resume = docx2txt.process(res)
        jobid = job.job_desc
        # print(job)
        text = [resume, jobid]
        cv = CountVectorizer(stop_words="english")
        count_matrix = cv.fit_transform(text)

        # print(cosine_similarity(count_matrix))

        match = cosine_similarity(count_matrix)[0][1]
        match = match * 100
        match = round(match, 2)
        # print(match)

        # return HttpResponse(match)
        match_per = str(match)
        messages.add_message(
            request, messages.SUCCESS, match_per)

        return redirect("index")
    context = {"job": job}
    return render(request, "track/view_profile.html", context)
