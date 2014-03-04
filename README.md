muni-crossing
=============

The aim of this repo is to end up with a web page that I can easily look at to figure out which stop I should use to transfer between perpendicular Muni lines such that I have the shortest wait.

For example, when taking the 33 eastbound, should I switch at Castro to the 24, or at Church to the J? [This XML](http://webservices.nextbus.com/service/publicXMLFeed?command=predictionsForMultiStops&a=sf-muni&stops=33|3326&stops=33|3323&stops=24|4315&stops=J|3987) tells me, but I have to do a bit of work to be able to build that XML document for any given route and its crossings. Let's see if I can manage it.

This builds on the [short gist](https://gist.github.com/blech/1223502) I wrote a few years ago.