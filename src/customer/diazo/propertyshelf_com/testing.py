# -*- coding: utf-8 -*-
"""Test Layer for customer.diazo.propertyshelf_com."""

# zope imports
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    PLONE_FIXTURE,
    applyProfile,
)
from plone.testing import (
    Layer,
    z2,
)
from zope.configuration import xmlconfig


class CustomerDiazoPropertyshelfComLayer(PloneSandboxLayer):
    """Custom Test Layer for customer.diazo.propertyshelf_com."""
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        """Set up Zope for testing."""
        # Load ZCML
        import customer.diazo.propertyshelf_com
        xmlconfig.file(
            'configure.zcml',
            customer.diazo.propertyshelf_com,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'customer.diazo.propertyshelf_com:default')


CUSTOMER_DIAZO_PROPERTYSHELF_COM_FIXTURE = CustomerDiazoPropertyshelfComLayer()


CUSTOMER_DIAZO_PROPERTYSHELF_COM_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CUSTOMER_DIAZO_PROPERTYSHELF_COM_FIXTURE,),
    name='CustomerDiazoPropertyshelfComLayer:IntegrationTesting'
)


CUSTOMER_DIAZO_PROPERTYSHELF_COM_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CUSTOMER_DIAZO_PROPERTYSHELF_COM_FIXTURE,),
    name='CustomerDiazoPropertyshelfComLayer:FunctionalTesting'
)


CUSTOMER_DIAZO_PROPERTYSHELF_COM_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CUSTOMER_DIAZO_PROPERTYSHELF_COM_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CustomerDiazoPropertyshelfComLayer:AcceptanceTesting'
)


ROBOT_TESTING = Layer(name='customer.diazo.propertyshelf_com:Robot')
