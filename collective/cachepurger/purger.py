from zope.app.cache import ram
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName


class PurgeView(BrowserView):

    def purge_caches(self):
        """Empties the different Zope RAM caches"""

        portal_url = getToolByName(self.context, "portal_url")
        portal = portal_url.getPortalObject()

        # 1) Recook css and js
        css_registry = portal.get('portal_css')
        css_registry.cookResources()

        js_registry = portal.get('portal_javascripts')
        js_registry.cookResources()

        # 2) Invalidate the global Z3 Ram cache that memoize uses as default.
        global_cache = ram.RAMCache()
        global_cache.invalidateAll()

        # 3) Run through Z2 RAM caches in Plone root
        for obj in portal.objectValues('RAM Cache Manager'):
            cache = obj.ZCacheManager_getCache()
            cache.cache = {}

        return "All caches has been purged"
