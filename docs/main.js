const startDate = new Date('2024-04-20T00:00:00');

// Starting timing
window.onload = function() {
    updateTimer();
    setInterval(updateTimer, 1000);
};

function updateTimer() {
    const now = new Date();
    const diffInSeconds = Math.floor((now - startDate) / 1000);

    // fix: Simplified handling, ignoring leap years.
    const days = Math.floor(diffInSeconds / (3600 * 24));
    const hours = Math.floor((diffInSeconds % (3600 * 24)) / 3600);
    const minutes = Math.floor((diffInSeconds % 3600) / 60);
    const seconds = diffInSeconds % 60;

    // formatting
    document.getElementById('timer1').textContent = `${diffInSeconds} seconds`
    document.getElementById('timer2').textContent = `${padZero(days)}天 ${padZero(hours)}小时 ${padZero(minutes)}分钟 ${padZero(seconds)}秒`;
}

function padZero(num) {
    return num.toString().padStart(2, '0');
}