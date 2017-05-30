from .default import home_page


def includeme(config):
    """List of views to include for config."""
    config.add_view(home_page, route_name='home')