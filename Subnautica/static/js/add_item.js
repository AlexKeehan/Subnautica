document.getElementById("select_model").addEventListener("change", function() {
    let model = this.value;
    const extraFieldsCont = document.getElementById("extra_fields");
    extraFieldsCont.innerHTML = '';

    const modelFields = {
        biomes: [
            { label: "Biome Name", name: "biome", placeholder: "Enter Biome Name" },
            { label: "Description", name: "description", placeholder: "Enter Description" },
            { label: "Short Description", name: "short_description", placeholder: "Enter Short Description" },
            { label: "Biome Type", name: "biome_type", placeholder: "Enter Biome Type" },
            { label: "Depth Range", name: "depth_range", placeholder: "Enter Depth Range" },
            { label: "Temperature Range", name: "temp_range", placeholder: "Enter Temperature Range" },
            { label: "Resources", name: "resources", placeholder: "Enter Resources" }
        ],
        eggs: [
            { label: "Egg Name", name: "egg", placeholder: "Enter Egg Name" },
            { label: "Description", name: "description", placeholder: "Enter Description" },
            { label: "Attitude", name: "attitude", placeholder: "Enter Attitude" },
            { label: "Locations", name: "locations", placeholder: "Enter Locations" }
        ],
        faunas: [
            { label: "Fauna", name: "fauna", placeholder: "Enter Fauna Name" },
            { label: "Description", name: "description", placeholder: "Enter Description" },
            { label: "Attitude", name: "attitude", placeholder: "Enter Attitude" },
            { label: "Fauna Type", name: "fauna_type", placeholder: "Enter Fauna Type" },
            { label: "Biomes", name: "biomes", placeholder: "Enter Biomes" },
        ],
        floras: [
            { label: "Flora Name", name: "flora", placeholder: "Enter Flora Name" },
            { label: "Description", name: "description", placeholder: "Enter Description" },
            { label: "Use", name: "use", placeholder: "Enter Use" },
            { label: "Attitude", name: "attitude", placeholder: "Enter Attitude" },
            { label: "Obtain From", name: "obtain_from", placeholder: "Enter Obtain From" },
            { label: "Biomes", name: "biomes", placeholder: "Enter Biomes" },
            { label: "Growth Time", name: "growth_time", placeholder: "Enter Growth Time" },
        ],
        resources: [
            { label: "Resource Name", name: "resource", placeholder: "Enter Resource Name" },
            { label: "Description", name: "description", placeholder: "Enter Description" },
            { label: "Obtain From", name: "obtain_from", placeholder: "Enter Obtain From" },
            { label: "Locations", name: "locations", placeholder: "Enter Locations" },
            { label: "Size", name: "size", placeholder: "Enter Size" },
        ],
        tools: [
            { label: "Tool Name", name: "tool", placeholder: "Enter Tool Name" },
            { label: "Description", name: "description", placeholder: "Enter Description" },
            { label: "Short Description", name: "short_description", placeholder: "Enter Short Description" },
            { label: "Tool Type", name: "tool_type", placeholder: "Enter Type" },
            { label: "Build Time", name: "build_time", placeholder: "Enter Build Time" },
            { label: "Attribute", name: "attribute", placeholder: "Enter Attribute" },
        ],
        vehicles: [
            { label: "Vehicle Name", name: "vehicle", placeholder: "Enter Vehicle Name" },
            { label: "Description", name: "description", placeholder: "Enter Description" },
            { label: "Short Description", name: "short_description", placeholder: "Enter Short Description" },
            { label: "Velocity", name: "velocity", placeholder: "Enter Velocity" },
            { label: "Health", name: "health", placeholder: "Enter Health" },
            { label: "Acquired From", name: "acq_from", placeholder: "Enter Acquired From" },
        ]
    };

    const fields = modelFields[model];
    if (fields) {
        fields.forEach(field => {
            const div = document.createElement('div');
            div.classList.add('input_info');

            const label = document.createElement('label');
            label.setAttribute('for', field.name);
            label.textContent = field.label;

            const input = document.createElement('input');
            input.setAttribute('type', 'text');
            input.setAttribute('id', field.name);
            input.setAttribute('name', field.name);
            input.setAttribute('placeholder', field.placeholder);

            div.appendChild(label);
            div.appendChild(input);
            extraFieldsCont.appendChild(div);
        });
    }
});

imageDisplay()