// 1
const kidNames = ["თამარი", "გიორგი", "მარიამი"]
kidNames.forEach(kidNames => {
    console.log("წარმატებები " + kidNames)
});
// 2
arrayOfNums = [3,5,4,6,7,10]
arrayOfNums.forEach(arrayOfNums => {
    console.log(arrayOfNums * 2)
});
// 3 
discountProducts = ["ლეპტოპი", "სმარტფონი", "მაგიდის ლამპა"]
discountProducts.forEach(discountProducts => {
    console.log("პროდუქტი " + discountProducts + " არის გაყიდვაში!")
});
// 4
dangerousAnimals = ["Raccoon", "Lion", "African Buffalo"]
dangerousAnimals.forEach(dangerousAnimals => {
    console.log(dangerousAnimals + " is a very dangerous species")
});
// 5
prices = [150, 125, 75]
prices.forEach(prices => {
    if (prices > 100)
        console.log(prices + " is Overpriced!")
    if (prices < 100)
        console.log(prices + " is not Overpriced")
});
// 6
function sameAsBefore() {
    array1 = ["O", "A", "E"]
    array2 = ["A", "E", "W"]
    array1.forEach(array1 => {
        if (array1 == array2)
            console.log(array1+array2)
        else
            console.log()
    });
}
// 7
function multiplication(a, b) {
    console.log(a * b)
}
// 8
function formatOfTime(yyyy, mm, dd) {
    console.log(`${yyyy}-${mm}-${dd}`)
}
// 9
dataTypes = [1, 8, "Hello, World!", true, 9]
dataTypes.forEach(dataTypes => {
    console.log(dataTypes.Math.max)
});
// 10
nums = [1,2,3,4,5]
nums.forEach(nums => {
    console.log(nums.Math.sum)
});
// 11
console.log("Couldn't do HW")
// 12
function ageChecking(num) {
    if (num > 18) {
        console.log("GET YOSELF A BEER KID!!!")
    }
    if (num < 18) {
        console.log("SKIDDADLE KID!!!")
    }
}
// 13
function requestQuestGuess(num) {
    console.log("Request: pick a number bigger than 5")
    if (num > 5)
        console.log("GOOD JOB!")
    if (num < 5)
        console.log("YOUR STREAK CREEK HAS BEEN TAKEN BY A FISH CRITIC")
}
// 14
console.log("Couldn't do HW")
// 15
function lenghtChecker(element) {
    let lenghtOfElement = element.length
    console.log(lenghtOfElement)
}