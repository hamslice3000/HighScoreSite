from django.contrib import admin
from django.urls import path

from entries import views as entries_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("index/", entries_views.index),
    path("indexweb/", entries_views.indexweb),
    path("indexHi/", entries_views.indexHi),
    path("indexLow/", entries_views.indexLow),
    path("indexLat/", entries_views.indexLat),
    path("latest/", entries_views.latest),
    path("three/", entries_views.three),
    path("lowest/", entries_views.lowest),
    path("add/", entries_views.add),
    path("lottery/", entries_views.lottery),
    path("lotteryCycle/", entries_views.lotteryCycle),
    path("lotteryWinner/", entries_views.lotteryWinner),
    path("vote/", entries_views.vote),
    path("voteweb/", entries_views.voteweb),
    path("voting/", entries_views.voting),
    path("votingcoin/", entries_views.votingcoin),
    path("voteup/", entries_views.voteup),
    path("votedown/", entries_views.votedown),
    path("votecoinup/", entries_views.votecoinup),
    path("votecoindown/", entries_views.votecoindown),
    path("entryup/", entries_views.entryup),
    path("entrydown/", entries_views.entrydown),
    path("enter/", entries_views.enter),
    path("top/", entries_views.top),
    path("random-entry/", entries_views.random_entry),
    path("vote-entry/", entries_views.vote_entry),
]