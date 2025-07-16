    const form = document.getElementById('formTag'); // ვინახავთ ფორმს ფორმტაგის მქონე id-ს ელემენტიდან

form.addEventListener('submit', (e) => { // გაშვება
    e.preventDefault();

    let textValue = e.target.elements.text.value;

    console.log(textValue);

    const ul = document.createElement('ul'); // ელემენტი "ულ" ის გადმოტანა
    const li = document.createElement('li'); // ელემენტი "ლი" ის გადმოტანა
    const Deletebtn = document.createElement('button'); // ელემენტი "წაშლის ღილაკის" ის გადმოტანა
    const editBtn = document.createElement('button');  // ელემენტი "შეცვლის ღილაკის" ის გადმოტანა
    Deletebtn.textContent = 'Delete';

    ul.appendChild(li);// ვამატებთ ელემენტ "ლი"-ს ვებსაიტში
    ul.appendChild(Deletebtn); // ვამატებთ ელემენტ "ლი"-ს ვებსაიტში
    ul.appendChild(editBtn); // ვამატებთ ელემენტ "ლი"-ს ვებსაიტში

    li.textContent = textValue;
    editBtn.textContent = 'Edit The Task'; // ტექსტი რაც ღილაკზე გამოვა

    Deletebtn.addEventListener('click', () => { // წაშლის ღილაკი როცა დააჭერ:
        ul.removeChild(li); // იშლება ლისტის ელემენტი
        ul.removeChild(Deletebtn); // წავშალოთ ღილაკი რომელსაც დავაჭირეთ
        ul.removeChild(editBtn); // წავშალოთ გვერძე-მყოფი ღილაკი
    });

    editBtn.addEventListener('click', () => { // როცა ვაჭერთ შეცვლის ღილაკს
        const edited = prompt('Please enter a text and edit the task'); // გამოიტანოს შეცვლის ფანჯარა
        li.textContent = edited; // მერე შევცვალოთ ძველი ტექსტი ამ ახალი ტექსტით
    })

    document.body.appendChild(ul); // დავამატოთ ყველა ელემენტი რაც დავწერეთ
});