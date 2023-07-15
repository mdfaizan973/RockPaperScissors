//  <!-- ---- -->
document.addEventListener("DOMContentLoaded", function () {
  const gameBoard = document.getElementById("game-board");
  const cellSize = 20;
  const boardSize = 400 / cellSize;
  const snake = [{ x: 10, y: 10 }];
  let food = { x: 5, y: 5 };
  let dx = 0;
  let dy = 0;
  let score = 0;
  let isChangingDirection = false;
  let gameInterval;

  // Generate random coordinates for the food
  function generateFood() {
    food = {
      x: Math.floor(Math.random() * boardSize),
      y: Math.floor(Math.random() * boardSize),
    };
  }

  // Move the snake
  function moveSnake() {
    const head = { x: snake[0].x + dx, y: snake[0].y + dy };
    snake.unshift(head);
    if (head.x === food.x && head.y === food.y) {
      generateFood();
      score++;
    } else {
      snake.pop();
    }
  }

  // Draw the game board
  function drawBoard() {
    gameBoard.innerHTML = "";

    // Draw snake
    snake.forEach((segment) => {
      const snakeElement = document.createElement("div");
      snakeElement.style.left = segment.x * cellSize + "px";
      snakeElement.style.top = segment.y * cellSize + "px";
      snakeElement.classList.add("cell");
      snakeElement.classList.add("snake");
      gameBoard.appendChild(snakeElement);
    });

    // Draw food
    const foodElement = document.createElement("div");
    foodElement.style.left = food.x * cellSize + "px";
    foodElement.style.top = food.y * cellSize + "px";
    foodElement.classList.add("cell");
    foodElement.classList.add("food");
    gameBoard.appendChild(foodElement);
  }

  // Change snake direction
  document.getElementById("up").addEventListener("click", () => {
    if (dy !== 1) {
      dx = 0;
      dy = -1;
      isChangingDirection = true;
    }
  });
  document.getElementById("down").addEventListener("click", () => {
    if (dy !== -1) {
      dx = 0;
      dy = 1;
      isChangingDirection = true;
    }
  });
  document.getElementById("left").addEventListener("click", () => {
    if (dx !== 1) {
      dx = -1;
      dy = 0;
      isChangingDirection = true;
    }
  });
  document.getElementById("right").addEventListener("click", () => {
    if (dx !== -1) {
      dx = 1;
      dy = 0;
      isChangingDirection = true;
    }
  });
  function changeDirection(event) {
    if (isChangingDirection) return;

    const keyPressed = event.key;
    switch (keyPressed) {
      case "ArrowUp":
        if (dy !== 1) {
          dx = 0;
          dy = -1;
          isChangingDirection = true;
        }
        break;
      case "ArrowDown":
        if (dy !== -1) {
          dx = 0;
          dy = 1;
          isChangingDirection = true;
        }
        break;
      case "ArrowLeft":
        if (dx !== 1) {
          dx = -1;
          dy = 0;
          isChangingDirection = true;
        }
        break;
      case "ArrowRight":
        if (dx !== -1) {
          dx = 1;
          dy = 0;
          isChangingDirection = true;
        }
        break;
    }

    clearInterval(gameInterval);
    gameInterval = setInterval(gameLoop, 125); // Reduced speed by 25%
  }

  // Game loop
  function gameLoop() {
    moveSnake();
    drawBoard();

    // Check for game over conditions
    const head = snake[0];
    if (
      head.x < 0 ||
      head.y < 0 ||
      head.x >= boardSize ||
      head.y >= boardSize ||
      isCollision()
    ) {
      clearInterval(gameInterval);
      swal(
        `Game Over! Your Score is ${score}`,
        "Please start again!",

        "error"
      );
      resetGame();
    }

    isChangingDirection = false;
    document.getElementById("scores").innerHTML = score;
  }
  // Check for collision with snake body
  function isCollision() {
    const head = snake[0];
    for (let i = 1; i < snake.length; i++) {
      if (snake[i].x === head.x && snake[i].y === head.y) {
        return true;
      }
    }
    return false;
  }

  // Reset the game
  function resetGame() {
    snake.length = 1;
    dx = 0;
    dy = 0;
    score = 0;
    generateFood();
    drawBoard();
  }

  // Start the game
  generateFood();
  drawBoard();
  gameInterval = setInterval(gameLoop, 125); // Initial speed
  document.addEventListener("keydown", changeDirection);
});
