document.getElementById("select_model").addEventListener("change", function() {
    let model = this.value;
    const extraFieldsCont = document.getElementById("extra_fields");
    extraFieldsCont.innerHTML = '';

    const modelFields = {
        biomes: [
            { label: "Biome Name", name: "name", placeholder: "Enter Biome Name" },
            { label: "Description", name: "description", placeholder: "Enter Description" },
            { label: "Short Description", name: "short_description", placeholder: "Enter Short Description" },
            { label: "Biome Type", name: "biome_type", placeholder: "Enter Biome Type" },
            { label: "Depth Range", name: "depth_range", placeholder: "Enter Depth Range" },
            { label: "Temperature Range", name: "temp_range", placeholder: "Enter Temperature Range" },
            { label: "Resources", name: "resources", isSelectMultiple: true },
        ],
        eggs: [
            { label: "Egg Name", name: "name", placeholder: "Enter Egg Name" },
            { label: "Description", name: "description", placeholder: "Enter Description" },
            { label: "Attitude", name: "attitude", placeholder: "Enter Attitude" },
            { label: "fauna", name: "fauna", isSelectMultiple: true },
            { label: "biomes", name: "biomes", isSelectMultiple: true },
        ],
        faunas: [
            { label: "Fauna", name: "name", placeholder: "Enter Fauna Name" },
            { label: "Description", name: "description", placeholder: "Enter Description" },
            { label: "Attitude", name: "attitude", placeholder: "Enter Attitude" },
            { label: "Fauna Type", name: "fauna_type", placeholder: "Enter Fauna Type" },
            { label: "Biomes", name: "biomes", isSelectMultiple: true },
        ],
        floras: [
            { label: "Flora Name", name: "name", placeholder: "Enter Flora Name" },
            { label: "Description", name: "description", placeholder: "Enter Description" },
            { label: "Use", name: "use", placeholder: "Enter Use" },
            { label: "Attitude", name: "attitude", placeholder: "Enter Attitude" },
            { label: "Obtain From", name: "obtain_from", placeholder: "Enter Obtain From" },
            { label: "Biomes", name: "biomes", isSelectMultiple: true },
            { label: "Growth Time", name: "growth_time", placeholder: "Enter Growth Time" },
        ],
        resources: [
            { label: "Resource Name", name: "name", placeholder: "Enter Resource Name" },
            { label: "Description", name: "description", placeholder: "Enter Description" },
            { label: "Obtain From", name: "obtain_from", placeholder: "Enter Obtain From" },
            { label: "biomes", name: "biomes", isSelectMultiple: true },
            { label: "Size", name: "size", placeholder: "Enter Size" },
        ],
        tools: [
            { label: "Tool Name", name: "name", placeholder: "Enter Tool Name" },
            { label: "Description", name: "description", placeholder: "Enter Description" },
            { label: "Short Description", name: "short_description", placeholder: "Enter Short Description" },
            { label: "Tool Type", name: "tool_type", placeholder: "Enter Type" },
            { label: "Build Time", name: "build_time", placeholder: "Enter Build Time" },
            { label: "Attribute", name: "attribute", placeholder: "Enter Attribute" },
        ],
        vehicles: [
            { label: "Vehicle Name", name: "name", placeholder: "Enter Vehicle Name" },
            { label: "Description", name: "description", placeholder: "Enter Description" },
            { label: "Short Description", name: "short_description", placeholder: "Enter Short Description" },
            { label: "Velocity", name: "velocity", placeholder: "Enter Velocity" },
            { label: "Health", name: "health", placeholder: "Enter Health" },
            { label: "Acquired From", name: "acq_from", placeholder: "Enter Acquired From" },
        ]
    };

    const url = `${getDropDownData}?model=${model}`;

    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        const fields = modelFields[model];
        if (fields) {
            fields.forEach(field => {
                const div = document.createElement('div');
                div.classList.add('input_info');

                const label = document.createElement('label');
                label.setAttribute('for', field.name);
                label.textContent = field.label;

                let input;
                if (field.isSelectMultiple) {
                    input = document.createElement('select');
                    input.setAttribute('id', field.name);
                    input.setAttribute('name', field.name);
                    input.setAttribute('multiple', 'multiple');
                    input.classList.add('dropdown');

                    if (field.name === "fauna" && data.faunas) {
                        data.faunas.forEach(fauna => {
                            const option = document.createElement("option");
                            option.value = fauna.id;
                            option.textContent = fauna.name;
                            input.appendChild(option);
                        })
                    }

                    if (field.name === "biomes" && data.biomes) {
                        data.biomes.forEach(biome => {
                            const option = document.createElement('option');
                            option.value = biome.id;
                            option.textContent = biome.name;
                            input.appendChild(option);
                        });
                    }
                } else {
                    input = document.createElement('input');
                    input.setAttribute('type', 'text');
                    input.setAttribute('id', field.name);
                    input.setAttribute('name', field.name);
                    input.setAttribute('placeholder', field.placeholder);
                }

                div.appendChild(label);
                div.appendChild(input);
                extraFieldsCont.appendChild(div);
            });
        }
    })
    .catch(error => console.error("Error Getting Data", error));
});

imageDisplay()