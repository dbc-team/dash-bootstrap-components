import pytest
import dash_bootstrap_components as dbc


class TestIconsModule:
    """Test suite for the icons module"""

    def test_bootstrap_icon_exists(self):
        """Test that Bootstrap icon set is defined"""
        assert hasattr(dbc.icons, "BOOTSTRAP")
        assert dbc.icons.BOOTSTRAP is not None

    def test_bootstrap_icon_is_string(self):
        """Test that Bootstrap icon is a string"""
        assert isinstance(dbc.icons.BOOTSTRAP, str)

    def test_bootstrap_icon_is_valid_url(self):
        """Test that Bootstrap icon URL is valid"""
        assert dbc.icons.BOOTSTRAP.startswith("https://")
        assert "bootstrap-icons" in dbc.icons.BOOTSTRAP

    def test_font_awesome_icon_exists(self):
        """Test that Font Awesome icon set is defined"""
        assert hasattr(dbc.icons, "FONT_AWESOME")
        assert dbc.icons.FONT_AWESOME is not None

    def test_font_awesome_icon_is_valid_url(self):
        """Test that Font Awesome icon URL is valid"""
        assert isinstance(dbc.icons.FONT_AWESOME, str)
        assert dbc.icons.FONT_AWESOME.startswith("https://")

    def test_remix_icon_exists(self):
        """Test that Remix icon set is defined"""
        assert hasattr(dbc.icons, "REMIX_ICON")
        assert dbc.icons.REMIX_ICON is not None

    def test_remix_icon_is_valid_url(self):
        """Test that Remix icon URL is valid"""
        assert isinstance(dbc.icons.REMIX_ICON, str)
        assert dbc.icons.REMIX_ICON.startswith("https://")
        assert "remixicon" in dbc.icons.REMIX_ICON

    def test_themify_icon_exists(self):
        """Test that Themify icon set is defined"""
        assert hasattr(dbc.icons, "THEMIFY")
        assert dbc.icons.THEMIFY is not None

    def test_themify_icon_is_valid_url(self):
        """Test that Themify icon URL is valid"""
        assert isinstance(dbc.icons.THEMIFY, str)
        assert dbc.icons.THEMIFY.startswith("https://")

    def test_boxicons_basic_exists(self):
        """Test that Boxicons Basic icon set is defined"""
        assert hasattr(dbc.icons, "BOXICONS_BASIC")
        assert dbc.icons.BOXICONS_BASIC is not None

    def test_boxicons_basic_is_valid_url(self):
        """Test that Boxicons Basic URL is valid"""
        assert isinstance(dbc.icons.BOXICONS_BASIC, str)
        assert dbc.icons.BOXICONS_BASIC.startswith("https://")
        assert "boxicons" in dbc.icons.BOXICONS_BASIC
        assert "basic" in dbc.icons.BOXICONS_BASIC

    def test_boxicons_filled_exists(self):
        """Test that Boxicons Filled icon set is defined"""
        assert hasattr(dbc.icons, "BOXICONS_FILLED")
        assert dbc.icons.BOXICONS_FILLED is not None

    def test_boxicons_filled_is_valid_url(self):
        """Test that Boxicons Filled URL is valid"""
        assert isinstance(dbc.icons.BOXICONS_FILLED, str)
        assert dbc.icons.BOXICONS_FILLED.startswith("https://")
        assert "boxicons" in dbc.icons.BOXICONS_FILLED
        assert "filled" in dbc.icons.BOXICONS_FILLED

    def test_boxicons_brands_exists(self):
        """Test that Boxicons Brands icon set is defined"""
        assert hasattr(dbc.icons, "BOXICONS_BRANDS")
        assert dbc.icons.BOXICONS_BRANDS is not None

    def test_boxicons_brands_is_valid_url(self):
        """Test that Boxicons Brands URL is valid"""
        assert isinstance(dbc.icons.BOXICONS_BRANDS, str)
        assert dbc.icons.BOXICONS_BRANDS.startswith("https://")
        assert "boxicons" in dbc.icons.BOXICONS_BRANDS
        assert "brands" in dbc.icons.BOXICONS_BRANDS

    def test_all_icon_sets_are_accessible(self):
        """Test that all icon sets are accessible from dbc.icons"""
        icon_sets = [
            "BOOTSTRAP",
            "FONT_AWESOME",
            "REMIX_ICON",
            "THEMIFY",
            "BOXICONS_BASIC",
            "BOXICONS_FILLED",
            "BOXICONS_BRANDS",
        ]
        for icon_set in icon_sets:
            assert hasattr(dbc.icons, icon_set), f"Icon set {icon_set} not found"
            assert isinstance(getattr(dbc.icons, icon_set), str)

