let TIME_LEFT = null;        // Stores selected duration in "MM:SS"
let remainingTime = null;    // Remaining time in seconds
let timerInterval = null;    // setInterval ID
let timerState = null;       // "running", "paused", "stopped"

const timerStates = {
  RUNNING: "running",
  PAUSED: "paused",
  STOPPED: "stopped"
};



document.addEventListener("DOMContentLoaded", () => {
  const durationButtons = document.querySelectorAll("button[name='duration']");
  const startBtn = document.getElementById("start");
  const pauseBtn = document.getElementById("pause");

  // Handle duration button click
  durationButtons.forEach(button => {
    button.addEventListener("click", function (event) {
      event.preventDefault();
      handleDurationClick(this);
    });
  });

  // Start button click
  startBtn.addEventListener("click", () => {
    if (!TIME_LEFT) return; // No time selected
    const [mins, secs] = TIME_LEFT.split(":").map(v => parseInt(v, 10));
    const totalSeconds = mins * 60 + secs;
    startTimer(totalSeconds);
  });

  // Pause / Resume button click
  pauseBtn.addEventListener("click", () => {
    handlePauseResume();
  });
});

// Pause / Resume handler
function handlePauseResume() {
  if (timerState === timerStates.RUNNING) {
    pauseTimer();
    document.getElementById("pause").textContent = "Resume";
  } else if (timerState === timerStates.PAUSED) {
    resumeTimer();
    document.getElementById("pause").textContent = "Pause";
  }
}

// When user clicks a time button
function handleDurationClick(button) {
  TIME_LEFT = button.value;
  highlightSelectionButton(button);

  const [mins, secs] = TIME_LEFT.split(":").map(v => parseInt(v, 10));
  updateWindow(mins * 60 + secs); // Show time immediately
}

// Timer finished popup
function popUpAfterTimer() {
  const userMessage = confirm("Time's Up! \nDo you want to add this to your history?");
  const choice = userMessage ? "Yes" : "No";
  document.getElementById("DialogBox");
}

// Start the timer
function startTimer(duration) {
  if (duration !== undefined) {
    remainingTime = duration;
  }
  updateWindow(remainingTime);
  timerState = timerStates.RUNNING;
  if (timerInterval) clearInterval(timerInterval);

  timerInterval = setInterval(() => {
    remainingTime--;

    if (remainingTime < 0) {
      clearInterval(timerInterval);
      document.getElementById("countdownClock").textContent = "Time's up!";
      popUpAfterTimer();
      timerState = timerStates.STOPPED;
      return;
    }
    updateWindow(remainingTime);
  }, 1000);
}

// Pause the timer
function pauseTimer() {
  if (timerState === timerStates.RUNNING) {
    clearInterval(timerInterval);
    timerState = timerStates.PAUSED;
  }
}

// Resume the timer
function resumeTimer() {
  if (timerState === timerStates.PAUSED) {
    startTimer(remainingTime); // Resume from where paused
  }
}

// Highlight the selected duration button
function highlightSelectionButton(selectedButton) {
  const allButtons = document.querySelectorAll("button[name='duration']");
  allButtons.forEach(button => {
    button.classList.remove("selected-time");
  });
  selectedButton.classList.add("selected-time");
}

// Update countdown display
function updateWindow(secondsLeft) {
  const mins = Math.floor(secondsLeft / 60);
  const secs = secondsLeft % 60;
  const display = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  document.getElementById("countdownClock").textContent = display;
}
