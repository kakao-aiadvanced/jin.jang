import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "What are the tourist attractions in Korea?"
            }
        ]
    )

    print(completion.choices[0].message.content)
'''
South Korea is rich in cultural heritage, natural beauty, and modern attractions. Here are some of the top tourist attractions across the country:

### Seoul
1. **Gyeongbokgung Palace**: The largest of the Five Grand Palaces, it features beautiful architecture and the National Folk Museum.
2. **N Seoul Tower**: Offering panoramic views of the city, this iconic tower is located on Namsan Mountain.
3. **Bukchon Hanok Village**: A traditional Korean village with painted hanoks (traditional houses), it's a great place to experience Korean culture.
4. **Myeongdong**: A vibrant shopping district known for cosmetics, fashion, and street food.
5. **Insadong**: A cultural district filled with traditional tea houses, craft shops, and galleries.

### Busan
1. **Haeundae Beach**: One of the most famous beaches in Korea, known for its festivals and nightlife.
2. **Gamcheon Culture Village**: A colorful hillside community with artistic murals and installations.
3. **Busan Tower**: Located in Yongdusan Park, it offers great views of the city and harbor.
4. **Jagalchi Fish Market**: A bustling seafood market offering fresh catches and unique culinary experiences.

### Jeju Island
1. **Hallasan National Park**: Home to Hallasan, South Korea's highest mountain, it offers hiking trails and beautiful landscapes.
2. **Seongsan Ilchulbong (Sunrise Peak)**: A UNESCO World Heritage site, it's famous for its stunning sunrises.
3. **Jeongbang Waterfall**: One of the few waterfalls in Asia that falls directly into the ocean.

### Gyeongju
1. **Bulguksa Temple**: Another UNESCO World Heritage site, known for its beautiful architecture and ancient relics.
2. **Seokguram Grotto**: An artificial cave with a magnificent Buddha statue, also a UNESCO site.
3. **Ancient Tombs of Daereungwon**: Historic burial sites of the Silla Kingdom with ancient tombs and artifacts.

### Incheon
1. **Songdo International Business District**: A modern city with stunning architecture, parks, and the Songdo Central Park.
2. **Incheon Chinatown**: The largest Chinatown in Korea, featuring Chinese restaurants, shops, and cultural experiences.

### DMZ (Demilitarized Zone)
1. **DMZ Tour**: A visit to this unique region offers insight into the history of the Korean Peninsula, including the Joint Security Area (JSA).

### Other Attractions
1. **Suwon Hwaseong Fortress**: A UNESCO World Heritage site with impressive fortifications from the late 18th century.
2. **Jinhae Cherry Blossom Festival**: Held in spring, it's one of Korea's most popular cherry blossom festivals.
3. **Nami Island**: A picturesque half-moon shaped island famous for its tree-lined paths and seasonal sceneries.

These attractions represent just a selection of what South Korea has to offer, blending history, culture, and natural beauty for visitors.
'''

if __name__ == '__main__':
    main()
