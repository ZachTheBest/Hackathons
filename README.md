# Los Altos Hacks - Moody Foody
Below is a sample sales pitch script designed for a three‐minute presentation with an additional one minute allocated for questions. You can adjust details as needed, but here’s a solid starting point:

[3-Minute Sales Pitch]
Hello Judges,
We are thrilled to present Moody Foody—the app that turns your mood into your next meal recommendation! Every day, millions of people face decision fatigue when choosing what to eat. What’s missing in the market is a solution that adapts to your feelings, culinary preferences, available ingredients, and even budget. That’s where Moody Foody comes in.
The Problem:
 Have you ever felt too tired or too stressed to decide what to cook or order? Traditional recipe apps and meal planners ignore the emotional and contextual factors that often dictate our cravings. Whether you’re in a celebratory mood, feeling down, or simply craving comfort food, you deserve a recommendation that matches your vibe.
Our Solution:
 Moody Foody leverages generative AI to provide personalized meal options in real time. Users simply input their mood, preferred cuisine, available ingredients, type of meal, health preference, dietary restrictions, and cost. Behind the scenes, our Flask-powered back end collects these inputs and crafts a custom prompt. This prompt is then sent to our generative AI via the Ollama API (using the Llama3 model), which generates three creative meal recommendations along with brief explanations. These recommendations are then seamlessly displayed on our single-page app, creating an interactive history of options for the user.
How We Built It:
 Our team developed Moody Foody as a full-stack application:
Front End: We built an intuitive single-page interface using HTML, CSS, and JavaScript. The app features dynamic elements like custom dropdowns and live updates, making it engaging and easy to use.


Back End: We used Python with Flask to handle form submissions. Once the user submits their preferences, our back end constructs a detailed prompt and calls the generative AI API through our helper function in ogollama.py.


Integration: The app uses asynchronous fetch requests to communicate between the client and server, ensuring that responses are displayed immediately without page reloads.


Challenges and Learnings:
 Integrating the AI API and managing asynchronous data flow were the biggest challenges. We learned to handle real-time API responses gracefully and to build a UI that updates dynamically. This project has not only deepened our understanding of full-stack development and AI integration but has also shown us how technology can bring personalization into everyday choices—transforming meal planning into a creative and enjoyable experience.
The Impact:
 Moody Foody is more than just a meal recommender; it’s a step toward a future where technology tailors everyday decisions to our unique lifestyles and emotions. Whether you want a healthy meal, a gourmet experience, or something fun and experimental, Moody Foody is here to help you decide—one mood at a time.
Thank you for your time and consideration. We’re excited to answer your questions now.

[1-Minute Q&A]
After your pitch, invite the judges:
"We’d love to hear any questions you have about Moody Foody—whether it’s about our technology stack, the AI integration, or our vision for the future of personalized meal planning. Thank you!"

This script should cover the key aspects of your project in a clear, concise manner while leaving room for an engaging Q&A session. Happy pitching!
