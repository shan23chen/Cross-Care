export interface DataType {
    slug: string;
    time: string;
    heading: string;
    heading2: string;
    date: string;
    imgSrc: string;
    authors: string;
    content: string;
}

export const postData: DataType[] = [
  {   
      slug: 'we-launch-delia',  
      time: "5 min",
      heading: 'We Launch Delia',
      heading2: 'Webflow this Week!',
      authors: "Jack Gallifant, Shan Chen",
      date: 'August 19, 2021',
      imgSrc: '/article.png',
      content: `
      Welcome to our blog! Here's a quick overview of what we'll cover:

      For a deeper dive into our methodologies, read our comprehensive guide [here](https://www.example.com/guide).

      ![Our Office](article.png)

      Check out our latest research on environmental policies [Environmental Study](https://www.example.com/environmental-study).

      Here's a snapshot of our recent field trip:

      ![Field Trip](article2.png)

      For further information, visit our project page at [Project Details](https://www.example.com/project-details).

      Thank you for reading! `,

  },
  { 
    slug: 'we-launch-delia2',  
    time: "5 min",
    heading: 'We Launch Delia1',
    heading2: 'Webflow this Week!',
    authors: "Published on Startupon",
    date: 'August 19, 2021',
    imgSrc: '/article2.png',
    content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde doloremque architecto pariatur sunt cum. Labore, eligendi ipsa consequatur impedit corrupti iure molestiae esse doloribus at officia a explicabo atque tempora!',

  },
  {
    slug: 'we-launch-delia3',  
    time: "5 min",
    heading: 'We Launch Delia2',
    heading2: 'Webflow this Week!',
    authors: "Published on Startupon",
    date: 'August 19, 2021',
    imgSrc: '/article3.png',
    content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde doloremque architecto pariatur sunt cum. Labore, eligendi ipsa consequatur impedit corrupti iure molestiae esse doloribus at officia a explicabo atque tempora!',
  },
  {
    slug: 'we-launch-delia4',  
    time: "5 min",
    heading: 'We Launch Delia3',
    heading2: 'Webflow this Week!',
    authors: "Published on Startupon",
    date: 'August 19, 2021',
    imgSrc: '/article.png',
    content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde doloremque architecto pariatur sunt cum. Labore, eligendi ipsa consequatur impedit corrupti iure molestiae esse doloribus at officia a explicabo atque tempora!',

  },
  {
    slug: 'we-launch-delia5',  
    time: "5 min",
    heading: 'We Launch Delia4',
    heading2: 'Webflow this Week!',
    authors: "Published on Startupon",
    date: 'August 19, 2021',
    imgSrc: '/article2.png',
    content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde doloremque architecto pariatur sunt cum. Labore, eligendi ipsa consequatur impedit corrupti iure molestiae esse doloribus at officia a explicabo atque tempora!',

  },
  {
    slug: 'we-launch-delia6',  
    time: "5 min",
    heading: 'We Launch Delia5',
    heading2: 'Webflow this Week!',
    authors: "Published on Startupon",
    date: 'August 19, 2021',
    imgSrc: '/article3.png',
    content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde doloremque architecto pariatur sunt cum. Labore, eligendi ipsa consequatur impedit corrupti iure molestiae esse doloribus at officia a explicabo atque tempora!',

  }
]

