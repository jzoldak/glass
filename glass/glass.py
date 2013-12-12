"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Boolean
from xblock.fragment import Fragment


class GlassXBlock(XBlock):
    """
    A testing block that checks the behavior of the container.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    pressed = Boolean(
        default=False, scope=Scope.user_state,
        help="Have you pressed the button yet?",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the GlassXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/glass.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/glass.css"))
        frag.add_javascript(self.resource_string("static/js/src/glass.js"))
        frag.initialize_js('GlassXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def button_press(self, data, suffix=''):
        """
        Press the button and do the thing
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.pressed = True
        return {"pressed": self.pressed}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("GlassXBlock",
             """<vertical_demo>
                <glass/>
                </vertical_demo>
             """
            ),
        ]
