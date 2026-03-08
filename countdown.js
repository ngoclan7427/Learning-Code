function startTimer(duration) {
    let timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        console.log(minutes + ":" + (seconds < 10 ? "0" : "") + seconds);

        if (--timer < 0) {
            console.log("Hết giờ!");
            timer = 0;
        }
    }, 1000);
}
startTimer(60); // Đếm ngược 60 giây
