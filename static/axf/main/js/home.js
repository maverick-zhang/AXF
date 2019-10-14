$(function () {
    top_swiper();
    must_by_swiper();

})
function top_swiper() {

        var swiper = new Swiper("#topSwiper", {
        loop: true,
        autoplay: 3000,
        pagination: '.swiper-pagination'
    });

}
function must_by_swiper() {
    var swiper = new Swiper("#swiperMenu",{
        slidesPerView : 3,
    });
}