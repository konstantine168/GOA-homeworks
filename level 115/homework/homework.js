const data = [
    {
        id: "6883a66d10aeac871f66b3a1",
        name: "Pia Papava",
        age: 1
    },
    {
        id: "6883a67b92c24ed7d9cf2d47",
        name: "konstantine",
        age: 10
    },
    {
        id: "6883a6809ce6d66f601dedd4",
        name: "Giorgi Papava",
        age: 38
    },
    {
        id: "6883a687e6cb99b0f229a2b3",
        name: "Nino Tevzadze",
        age: 39
    }
]
function handleInputChange() {
        const search = document.getElementById('s1');
        console.log(search)
        search.onclick = (event) => {
            const value = event.target.value
            console.log(value)
        }
        data.map((item) => {
            const div = document.createElement("div")
            const nameSearch =  document.getElementById("nameSearch")
            div.textContent = item.name
            nameSearch.append(div)
            console.log(nameSearch)
        })
}