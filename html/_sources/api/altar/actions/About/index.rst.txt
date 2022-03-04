:mod:`altar.actions.About`
==========================

.. py:module:: altar.actions.About


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.actions.About.About



.. py:class:: About(name, spec, plexus, **kwds)

   Bases: :class:`altar.panel()`

   Display information about this application

   .. attribute:: root
      

      

   .. attribute:: tip
      :annotation: = specify the portion of the namespace to display

      

   .. method:: name(self, plexus, **kwds)

      Print the name of the app for configuration purposes


   .. method:: home(self, plexus, **kwds)

      Print the application home directory


   .. method:: prefix(self, plexus, **kwds)

      Print the application installation directory


   .. method:: models(self, plexus, **kwds)

      Print the altar model directory


   .. method:: when(self, plexus, **kwds)

      Print the build timestamp


   .. method:: etc(self, plexus, **kwds)

      Print the application configuration directory


   .. method:: version(self, plexus, **kwds)

      Print the version of the altar package


   .. method:: copyright(self, plexus, **kwds)

      Print the copyright note of the altar package


   .. method:: credits(self, plexus, **kwds)

      Print out the license and terms of use of the altar package


   .. method:: license(self, plexus, **kwds)

      Print out the license and terms of use of the altar package


   .. method:: nfs(self, plexus, **kwds)

      Dump the application configuration namespace


   .. method:: pfs(self, plexus, **kwds)

      Dump the application private filesystem


   .. method:: vfs(self, plexus, **kwds)

      Dump the application virtual filesystem



