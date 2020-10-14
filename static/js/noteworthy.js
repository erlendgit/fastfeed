/**
 * Identify noteworthy items by the distance between two
 * items of the same site in relation to the total number
 * of articles on the page.
 */
(function ($) {
    var articleStore = {};
    var articleScores = [];
    var articles = $('.articles .article');

    articles.each(function (i, article) {
        var siteName = $(article).data('site');
        var lastArticle = articleStore[siteName];

        if (lastArticle !== undefined) {
            articleScores[lastArticle.i] = {
                article: lastArticle.article,
                score: i - lastArticle.i
            };
        }
        articleStore[siteName] = {
            article: $(article),
            i: i,
        };
    });

    var ref = articles.length / 5;
    articles.each(function (i, article) {
        var score = articleScores[i] && articleScores[i].score;
        if (score >= ref) {
            $(article).addClass('special');
        }
    });
})(jQuery);