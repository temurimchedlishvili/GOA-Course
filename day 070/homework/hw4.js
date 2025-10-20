// ელემენტის წამოღება ID-თი
const title = document.getElementById('title');
const button = document.getElementById('changeStyleBtn');

// ღილაკზე დაჭერისას შევცვალოთ სტილი
button.addEventListener('click', () => {
title.style.color = 'tomato';
title.style.backgroundColor = 'black';
title.style.padding = '10px 20px';
title.style.borderRadius = '8px';
title.style.textAlign = 'center';
});
