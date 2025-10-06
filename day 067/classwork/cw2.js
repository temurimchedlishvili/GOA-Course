function compare(student1, student2) {
  // ჯერ ვადარებთ grade-ს
if (student1.grade > student2.grade) {
    return student1.name;
} else if (student1.grade < student2.grade) {
    return student2.name;
} else {
    // თუ grade-ები თანაბარია, ვადარებთ id-ს
    if (student1.id < student2.id) {
    return student1.name;
    } else if (student1.id > student2.id) {
    return student2.name;
    } else {
    return "ორივე თანაბარია";
    }
}
}


const s1 = { name: "გიორგი", id: 2, grade: 90 };
const s2 = { name: "ნიკა", id: 1, grade: 90 };

console.log(compare(s1, s2)); 
