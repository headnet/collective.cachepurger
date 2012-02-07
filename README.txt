collective.cachepurger
======================

Cachepurger scraches a small itch. We've experienced that when we deploy a new 
version of a Plone package, it does not behave as expected even though it did 
at the test server. One reason is that the resource registries or caches contains 
old data.

Cachepurge simply empties the different Zope RAM caches and rebuilds CSS and 
Javascript from the registries.

Just call http://mysite/@@purge-caches


/Anton



