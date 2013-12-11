/* Javascript for GlassXBlock. */
function GlassXBlock(runtime, element) {

    function sayPressed(result) {
        $('p#bpressed', element).text(result.pressed);
    }

    var handlerUrl = runtime.handlerUrl(element, 'button_press');

    $('button#pushme', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world"}),
            success: sayPressed
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
