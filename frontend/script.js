const form = document.getElementById("comicForm");
const result = document.getElementById("result");

form.addEventListener("submit", async function(e) {

    e.preventDefault();

    const button = form.querySelector("button");

    button.disabled = true;
    button.textContent = "⏳ Generating...";

    const data = {
        story_prompt:
            document.getElementById("story_prompt").value,

        character_name:
            document.getElementById("character_name").value,

        setting:
            document.getElementById("setting").value,

        tone:
            document.getElementById("tone").value,

        art_style:
            document.getElementById("art_style").value
    };

    try {

        const response = await fetch(
            "/generate",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }
        );

        const comic = await response.json();

        result.innerHTML =
            `<h2 style="color:white">
                ${comic.title}
            </h2>`;

        comic.panels.forEach(panel => {

            result.innerHTML += `
                <div class="panel">

                    <h3>
                        Panel ${panel.panel}
                    </h3>

                    <p>
                        ${panel.scene}
                    </p>

                    <div class="dialogue">
                        ${panel.dialogue}
                    </div>

                    <p>
                        🎨 ${panel.style}
                    </p>

                </div>
            `;

        });

    } catch (error) {

        result.innerHTML =
            `<div class="panel">
                ❌ Server connection error
            </div>`;

    }

    button.disabled = false;
    button.textContent = "✨ Generate Comic";

});
