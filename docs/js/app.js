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

    $(".tweet-right").click(function () {
        // print('clicked');
        // print('current tweet:', currentTweet);
        for (var i = 1; i < totalTweets + 1; i++) {
            print('i', i);
            if (i === currentTweet) {
                console.log(currentTweet);
                $('#tweet-' + i.toString()).addClass("show").removeClass("hidden");
                $('#tweet-info-' + i.toString()).addClass("show").removeClass("hidden");
            } else if (i != currentTweet + 1) {
                console.log(currentTweet);
                $('#tweet-' + i.toString()).addClass("hidden").removeClass("show");
                $('#tweet-info-' + i.toString()).addClass("hidden").removeClass("show");
            }
        }
        if (currentTweet === totalTweets) {
            currentTweet = 1;
        } else {
            currentTweet += 1;
        }
    });
    $(".tweet-left").click(function () {
        // print('clicked');
        // print('current tweet:', currentTweet);
        for (var i = 1; i < totalTweets + 1; i++) {
            // print('i', i);
            if (i === currentTweet) {
                $('#tweet-' + i.toString()).addClass("show").removeClass("hidden");
                $('#tweet-info-' + i.toString()).addClass("show").removeClass("hidden");
            } else if (i != currentTweet + 1) {
                $('#tweet-' + i.toString()).addClass("hidden").removeClass("show");
                $('#tweet-info-' + i.toString()).addClass("hidden").removeClass("show");
            }
        }
        if (currentTweet === 1) {
            currentTweet = totalTweets;
        } else {
            currentTweet -= 1;
        }
    });

    $(".delete").click(function () {
        $(this).closest(".notification").remove();
    });
}); // end