#!/bin/bash

# SkillVerse Installation Script

# Destination directory for Hermes Agent skills
SKILLS_DIR="$HOME/.hermes/skills"

# Create the skills directory if it doesn't exist
mkdir -p "$SKILLS_DIR"

# Clone the repository if it doesn't exist
if [ ! -d "SkillVerse" ]; then
    echo "Cloning SkillVerse repository..."
    git clone https://github.com/KusalPabasara/SkillVerse.git
fi

# Enter the repository
cd SkillVerse

# Create symbolic links for each skill
for skill in $(ls -d */ | grep -v 'scripts'); do
    skill_name=$(basename "$skill")
    ln -s "$(pwd)/$skill_name" "$SKILLS_DIR/$skill_name"
    echo "Installed skill: $skill_name"
done

echo "SkillVerse installation complete!"
echo "You can now use the SkillVerse skills with your Hermes Agent."
