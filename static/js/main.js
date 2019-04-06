var searchPageShown = false;

$(document).ready(function () {
    $("#search-button").click(function () {
        if (!searchPageShown) {
            $(".responsive-search-page").css("display", "block");
        } else {
            $(".responsive-search-page").css("display", "none");
        }
        searchPageShown = !searchPageShown;
    });

    $("#search-cross").click(function () {
        $(".responsive-search-page").css("display", "none");
        searchPageShown = false;
    });
});