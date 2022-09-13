$(document).ready(function () {
    /*
      >>> print('a', 'b', 'c');
      a b c
    */
    function print() {
        var sep = ' ';
        var toprint = '';
        for (var i = arguments.length - 1; i >= 0; i--) {
            arg = arguments[arguments.length - i - 1];
            if (typeof arg === 'string' || arg instanceof String) {

            } else {
                arg = arg.toString();
            }
            toprint += arg + sep;
        }
        console.log(toprint);
    }


    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function () {

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");

    });
    var currentTweet = 1;
    var totalTweets = 2;

    for (var i = 1; i < totalTweets + 1; i++) {
            
        if (i === 1) {

        } else{
            $('#tweet-' + i.toString()).hide();
            $('#tweet-info-' + i.toString()).hide();
            //$('#tweet-info-' + i.toString()).toggle();
        }
    }
    $(".tweet-right").click(function () {
        // print('clicked');
        // print('current tweet:', currentTweet);
        currentTweet += 1;

        if (currentTweet > totalTweets) {
            currentTweet = 1;
        }
        for (var i = 1; i < totalTweets + 1; i++) {
            if (i === currentTweet) {
                //print('currentTweet', i.toString())
                $('#tweet-' + i.toString()).show();
                $('#tweet-info-' + i.toString()).show();
                //$('#tweet-info-' + i.toString()).toggle();
                //print('i', i, 'currentTweet', currentTweet, '#tweet-info-' + i.toString());
            } else if (i != currentTweet) {
                $('#tweet-' + i.toString()).hide();
                $('#tweet-info-' + i.toString()).hide();
                //$('#tweet-info-' + i.toString()).toggle();
            }
        }
    });
    $(".tweet-left").click(function () {
        // print('clicked');
        // print('current tweet:', currentTweet);
        currentTweet -= 1;

        if (currentTweet < 1) {
            currentTweet = totalTweets;
        }
        for (var i = 1; i < totalTweets + 1; i++) {
            
            if (i === currentTweet) {
                //print('currentTweet', i.toString())
                $('#tweet-' + i.toString()).show();
                $('#tweet-info-' + i.toString()).show();
                //$('#tweet-info-' + i.toString()).toggle();
                //print('i', i, 'currentTweet', currentTweet, '#tweet-info-' + i.toString());
            } else if (i != currentTweet) {
                $('#tweet-' + i.toString()).hide();
                $('#tweet-info-' + i.toString()).hide();
                //$('#tweet-info-' + i.toString()).toggle();
            }
        }
    });

    $(".delete").click(function () {
        $(this).closest(".notification").remove();
    });
}); // end