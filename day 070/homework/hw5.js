// ელემენტების წამოღება class-ით
const titles = document.querySelectorAll('.title');
const button = document.getElementById('changeStyleBtn');

// ღილაკზე დაჭერისას თითოეულს ვცვლით სტილს
button.addEventListener('click', () => {
for (let i = 0; i < titles.length; i++) {
    titles[i].style.color = `hsl(${i * 60}, 80%, 50%)`; // განსხვავებული ფერი თითოეულს
    titles[i].style.backgroundColor = '#111827';
    titles[i].style.padding = '10px 15px';
    titles[i].style.borderRadius = '8px';
    titles[i].style.textAlign = 'center';
}
});
