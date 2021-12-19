console.log("asdf");
const inputField = document.getElementById("chat_text_input");
inputField.addEventListener("keydown", function (e) {
    if (e.code === "Enter") {
        console.log("keypress done");
        let input = inputField.value;
        inputField.value = "";
        let chat_area = document.getElementById("chat_text_area");
        let input_msg_div = document.createElement("div");
        input_msg_div.id="user";
        input_msg_div.innerText=input;
        input_msg_div.innerHTML=input;
        chat_area.appendChild(input_msg_div);
    }
});