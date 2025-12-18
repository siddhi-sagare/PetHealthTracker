document.addEventListener('DOMContentLoaded', () => {
    const leftArrow = document.querySelector(".left-arrow");
    const rightArrow = document.querySelector(".right-arrow");
    const slider = document.querySelector(".review-slider");
    const scrollAmount = 270; // width of slide + gap

    rightArrow.addEventListener("click", () => {
        slider.scrollBy({ left: scrollAmount, behavior: "smooth" });
    });

    leftArrow.addEventListener("click", () => {
        slider.scrollBy({ left: -scrollAmount, behavior: "smooth" });
    });
});
