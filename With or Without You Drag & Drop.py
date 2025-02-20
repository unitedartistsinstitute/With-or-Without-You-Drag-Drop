Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>With or Without You :: U2 :: Drag & Drop Activity</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            background-color: #f0f8ff;
        }
        .container {
            display: flex;
            width: 100%;
            gap: 20px;
            flex-grow: 1;
        }
        .word-bank {
            width: 25%;
            padding: 15px;
            background: #e6f3ff;
            border-radius: 8px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            position: sticky;
            top: 20px;
            max-height: 80vh;
            overflow-y: auto;
        }
        .lyrics-container {
            flex: 1;
            padding: 15px;
            background: light skyblue;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .word-item {
            padding: 10px;
            background: #007bff;
            color: white;
            border-radius: 4px;
            cursor: move;
            transition: transform 0.2s;
        }
        .word-item:hover {
            transform: translateX(5px);
        }
        .blank {
            display: inline-block;
            width: 150px;
            height: 24px;
            border-bottom: 2px solid #007bff;
            margin: 0 5px;
            vertical-align: bottom;
            text-align: center;
        }
        .filled {
            background: #e6f3ff;
        }
        iframe {
            margin-bottom: 20px;
            border-radius: 8px;
            width: 100%;
            height: 400px;
        }
        .score-board {
            padding: 20px;
            background: #e6f3ff;
            border-radius: 8px;
            margin-top: 20px;
        }
        #feedback {
            margin-top: 20px;
            padding: 15px;
            border-radius: 8px;
            display: none;
        }
        .correct { background: #d4edda !important; }
        .incorrect { background: #f8d7da !important; }
        .signature {
            margin-top: 30px;
            text-align: center;
            font-size: 0.9em;
            color: #666;
        }
        .signature a {
            color: #007bff;
            text-decoration: none;
        }
        .signature a:hover {
            text-decoration: underline;
        }
        .hidden {
            display: none;
        }
        .blank[data-filled="true"] {
            cursor: pointer;
        }
    </style>
    
</head>
<body>
    <h1>With or Without You :: U2 :: Drag & Drop Activity</h1>
    
    <iframe src="https://www.dailymotion.com/embed/video/x2qtw3i" 
            allowfullscreen 
            allow="autoplay"
            style="border:none">
    </iframe>

    <div class="container">
        <div class="word-bank" id="wordBank"></div>
        
        <div class="lyrics-container">
            <div class="lyrics">
                <p>See the <span class="blank" data-answer="stone"></span> set in your eyes</p>
                <p>See the thorn twist in your side</p>
                <p>I'll wait for you</p>
                <p><span class="blank" data-answer="Sleight of hand"></span> and <span class="blank" data-answer="twist of fate"></span></p>
                <p>On a <span class="blank" data-answer="bed of nails"></span>, she makes me wait</p>
                <p>And I wait without you</p>
                <p>With or without you... With or without you.</p>
                <p><span class="blank" data-answer="Through"></span> the <span class="blank" data-answer="storm"></span>, we reach the <span class="blank" data-answer="shore"></span></p>
                <p>You give it all but I want more</p>
                <p>And I'm waiting for you.</p>
                <p>With or without you ... With or without you Oh... </p>
                <p>I can't live, with or without you.</p> 
                <p>And you <span class="blank" data-answer="give yourself away"></span></p>
                <p>And you give yourself away.</p>
                <p>And you give, and you give</p>
                <p>And you give yourself away.</p>
                <p>My hands are <span class="blank" data-answer="tied"></span></p>
                <p>My body <span class="blank" data-answer="bruised"></span></p>
                <p>She's got me with</p>
                <p>Nothing to win and nothing left to lose</p>
            </div>
            
            <div class="score-board">
                <button onclick="checkAnswers()" style="background:#28a745;color:white;padding:10px 20px;border:none;border-radius:4px;cursor:pointer;">
                    Check Answers
                </button>
                <button onclick="resetActivity()" style="background:#dc3545;color:white;padding:10px 20px;border:none;border-radius:4px;cursor:pointer;margin-left:10px;">
                    Reset
                </button>
                <div id="feedback"></div>
            </div>
        </div>
    </div>

    <div class="signature">
        &copy; 2025 Daniel Rojas :: TΣʃ ::  &#9993; <a href="mailto:unitedartistsinstitute@gmail.com">unitedartistsinstitute@gmail.com</a>
    </div>

    <script>
        const targetWords = [
            'stone', 'Sleight of hand', 'twist of fate', 'bed of nails',
            'Through', 'storm', 'shore', 'give yourself away', 'tied', 'bruised'
        ];

        // Store word-blank associations
        let wordAssociations = {};

        function shuffle(array) {
            let shuffled = [...array];
            for (let i = shuffled.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
            }
            return shuffled;
        }

        function initializeWordBank() {
            const bank = document.getElementById('wordBank');
            bank.innerHTML = ''; // Clear the bank first if resetting
            
            shuffle(targetWords).forEach(word => {
                const div = document.createElement('div');
                div.className = 'word-item';
                div.id = 'word-' + Math.random().toString(36).substr(2, 9);
                div.draggable = true;
                div.textContent = word;
                div.setAttribute('data-word', word);
                div.ondragstart = drag;
                bank.appendChild(div);
            });
        }

        function drag(ev) {
            ev.dataTransfer.setData("text", ev.target.id);
            ev.dataTransfer.setData("word", ev.target.getAttribute('data-word'));
        }

        function allowDrop(ev) {
            ev.preventDefault();
        }

        function drop(ev) {
            ev.preventDefault();
            if (ev.target.classList.contains('blank')) {
                const wordId = ev.dataTransfer.getData("text");
                const wordText = ev.dataTransfer.getData("word");
                const wordElement = document.getElementById(wordId);
                
                // If this blank already had a word, return that word to the bank
                if (ev.target.getAttribute('data-filled') === 'true') {
                    returnWordToBank(ev.target.getAttribute('data-word-id'));
                }
                
                // Update the blank
                ev.target.textContent = wordText;
                ev.target.classList.add('filled');
                ev.target.setAttribute('data-filled', 'true');
                ev.target.setAttribute('data-word-id', wordId);
                ev.target.setAttribute('data-word', wordText);
                ev.target.onclick = function() { returnToBank(this); };
                
                // Hide the word in the bank
                if (wordElement) {
                    wordElement.classList.add('hidden');
                }
                
                // Store this association
                wordAssociations[wordId] = ev.target;
            }
        }

        function returnToBank(blankElement) {
            const wordId = blankElement.getAttribute('data-word-id');
            returnWordToBank(wordId);
            
            // Clear the blank
            blankElement.textContent = '';
            blankElement.classList.remove('filled');
            blankElement.removeAttribute('data-filled');
            blankElement.removeAttribute('data-word-id');
            blankElement.removeAttribute('data-word');
            blankElement.onclick = null;
        }
        
        function returnWordToBank(wordId) {
            if (wordId) {
                const wordElement = document.getElementById(wordId);
                if (wordElement) {
                    wordElement.classList.remove('hidden');
                }
            }
...         }
... 
...         function checkAnswers() {
...             let correct = 0;
...             document.querySelectorAll('.blank').forEach(blank => {
...                 const userAnswer = blank.textContent.trim();
...                 const correctAnswer = blank.dataset.answer.toLowerCase();
...                 
...                 blank.classList.remove('correct', 'incorrect');
...                 if (userAnswer.toLowerCase() === correctAnswer) {
...                     blank.classList.add('correct');
...                     correct++;
...                 } else if (userAnswer) {
...                     blank.classList.add('incorrect');
...                 }
...             });
... 
...             const feedback = document.getElementById('feedback');
...             feedback.style.display = 'block';
...             feedback.innerHTML = `
...                 <strong>Score: ${correct}/${targetWords.length}</strong><br>
...                 ${correct === targetWords.length ? 'Perfect! You did great! 🎉' : 
...                  correct >= 7 ? 'Good job! Keep practicing! ✨' :
...                  'Review the lyrics and try again! 💪'}
...             `;
...         }
...         
...         function resetActivity() {
...             // Clear all blanks
...             document.querySelectorAll('.blank').forEach(blank => {
...                 blank.textContent = '';
...                 blank.classList.remove('filled', 'correct', 'incorrect');
...                 blank.removeAttribute('data-filled');
...                 blank.removeAttribute('data-word-id');
...                 blank.removeAttribute('data-word');
...                 blank.onclick = null;
...             });
...             
...             // Hide feedback
...             document.getElementById('feedback').style.display = 'none';
...             
...             // Reset and reinitialize word bank
...             wordAssociations = {};
...             initializeWordBank();
...         }
... 
...         // Initialize draggable words and drop zones
...         window.onload = () => {
...             initializeWordBank();
...             document.querySelectorAll('.blank').forEach(blank => {
...                 blank.ondragover = allowDrop;
...                 blank.ondrop = drop;
...             });
...         };
...     </script>
... </body>
