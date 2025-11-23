import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

roommate_data = [
    {
        "category": "IDENTIFICATION",
        "traits": [
            "Subject ID: 'The Roommate'",
            "Name: 'Maya'",
            "Age: 24",
            "Occupation: Architecture Student / Barista"
        ]
    },
    {
        "category": "PHYSICAL METRICS",
        "traits": [
            "Height: 5'7\" (170 cm)",
            "Build: Slender, poor posture from drafting tables",
            "Skin Tone: Warm Olive",
            "Hair: Dark brown, perpetually in a messy bun",
            "Eyes: Hazel, usually squinting at a screen"
        ]
    },
    {
        "category": "APPAREL & AESTHETIC",
        "traits": [
            "Top: Oversized vintage university sweatshirt (stolen)",
            "Bottoms: Black leggings (covered in cat hair)",
            "Footwear: Fuzzy socks inside Crocs",
            "Accessories: Blue light glasses, silver nose ring"
        ]
    },
    {
        "category": "BEHAVIORAL QUIRKS",
        "traits": [
            "Diet: 80% Iced Coffee, 20% Instant Ramen",
            "Sleep Cycle: Nocturnal (Active 11 PM - 4 AM)",
            "Volume Level: Hums lo-fi beats unconsciously",
            "Hazard Level: Leaves dishes in sink for 3-5 business days"
        ]
    }
]

print("INITIALIZING ROOMMATE SURVEILLANCE PROTOCOL...")
time.sleep(2)

cycle_count = 1

try:
    while True:
        clear_screen()
        print(f"=== CYCLE {cycle_count} IN PROGRESS ===")
        print("Target acquired.\n")

        for section in roommate_data:
            print("-" * 40)
            print(f"   SCANNING SECTOR: {section['category']}")
            print("-" * 40)
            
            for trait in section['traits']:
                print(f" > {trait}")
            
            print("\n[Status] Processing next data packet...\n")
            time.sleep(5)

        print("Cycle complete. Rebooting scan sequence...")
        time.sleep(2)
        cycle_count += 1
except KeyboardInterrupt:
    print("\nProcess terminated.")

