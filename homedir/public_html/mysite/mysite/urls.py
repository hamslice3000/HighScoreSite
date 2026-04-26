from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'entries.views.index'),
    url(r'^indexweb/$', 'entries.views.indexweb'),
    url(r'^indexHi/$', 'entries.views.indexHi'),
    url(r'^indexLow/$', 'entries.views.indexLow'),
    url(r'^indexLat/$', 'entries.views.indexLat'),
    url(r'^latest/$', 'entries.views.latest'),
    url(r'^three/$', 'entries.views.three'),
    url(r'^lowest/$', 'entries.views.lowest'),
    url(r'^add/$', 'entries.views.add'),
    url(r'^lottery/$', 'entries.views.lottery'),
    url(r'^lotteryCycle/$', 'entries.views.lotteryCycle'),
    url(r'^lotteryWinner/$', 'entries.views.lotteryWinner'),
    url(r'^vote/$', 'entries.views.vote'),
    url(r'^voteweb/$', 'entries.views.voteweb'),
    url(r'^voting/$', 'entries.views.voting'),
    url(r'^votingcoin/$', 'entries.views.votingcoin'),
    url(r'^voteup/$', 'entries.views.voteup'),
    url(r'^votedown/$', 'entries.views.votedown'),
    url(r'^votecoinup/$', 'entries.views.votecoinup'),
    url(r'^votecoindown/$', 'entries.views.votecoindown'),
    url(r'^entryup/$', 'entries.views.entryup'),
    url(r'^entrydown/$', 'entries.views.entrydown'),
    url(r'^enter/$', 'entries.views.enter'),
    url(r'^top/$', 'entries.views.top'),
    url(r'^random-entry/$', 'entries.views.random_entry'),
    url(r'^vote-entry/$', 'entries.views.vote_entry'),
)