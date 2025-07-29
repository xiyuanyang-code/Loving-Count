const startDate = new Date('2024-04-20T00:00:00');

// Update timer every second
window.onload = function() {
    updateTimer();
    setInterval(updateTimer, 1000);
    fetchScores();                  // Initial fetch
    setInterval(fetchScores, 60000);// Update scores every 1 minute
};

function updateTimer() {
    const now = new Date();
    const diffInSeconds = Math.floor((now - startDate) / 1000);

    const days = Math.floor(diffInSeconds / (3600 * 24));
    const hours = Math.floor((diffInSeconds % (3600 * 24)) / 3600);
    const minutes = Math.floor((diffInSeconds % 3600) / 60);
    const seconds = diffInSeconds % 60;

    document.getElementById('timer1').textContent = `${diffInSeconds} seconds`;
    document.getElementById('timer2').textContent = `${padZero(days)}天 ${padZero(hours)}小时 ${padZero(minutes)}分钟 ${padZero(seconds)}秒`;
}

function padZero(num) {
    return num.toString().padStart(2, '0');
}

// Fetch scores from data.json and update the DOM
function fetchScores() {
    fetch('../data/data.json')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Find scores for yanyan and xiaoyuan
                const yanyan = data.find(user => user.name === 'yanyan');
                const xiaoyuan = data.find(user => user.name === 'xiaoyuan');
                // Update or create score display
                let scoreDiv = document.getElementById('score-board');
                if (!scoreDiv) {
                    scoreDiv = document.createElement('div');
                    scoreDiv.id = 'score-board';
                    scoreDiv.style.marginTop = '20px';
                    document.querySelector('.container').appendChild(scoreDiv);
                }
                scoreDiv.innerHTML = `
                <div>Yanyan's Score: <span style="color:black">${yanyan ? yanyan.score : 'N/A'}</span></div>
                <div>Xiaoyuan's Score: <span style="color:black">${xiaoyuan ? xiaoyuan.score : 'N/A'}</span></div>
            `;
            })
            .catch(error => {
                console.error('Error fetching scores:', error);
            });
}