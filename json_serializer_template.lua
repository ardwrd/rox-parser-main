-- Stream JSON serialization to avoid huge in-memory strings
local function escape_json_string(value)
    local escaped = value:gsub("\\", "\\\\")
    escaped = escaped:gsub("\"", "\\\"")
    escaped = escaped:gsub("\n", "\\n")
    escaped = escaped:gsub("\r", "\\r")
    escaped = escaped:gsub("\t", "\\t")
    return escaped
end

local function write_json(file, value)
    local value_type = type(value)
    if value_type == "table" then
        file:write("{")
        local first = true
        for k, v in pairs(value) do
            if not first then
                file:write(",")
            else
                first = false
            end
            file:write('"', tostring(k), '":')
            write_json(file, v)
        end
        file:write("}")
    elseif value_type == "number" or value_type == "boolean" then
        file:write(tostring(value))
    elseif value_type == "string" then
        file:write('"', escape_json_string(value), '"')
    else
        file:write("null")
    end
end

{{TABLE}}

-- Combine the attributes
for k, v in pairs({{FILE_NAME}}) do
  for attr_key, attr_value in pairs(__default_values) do
      if v[attr_key] == nil then
          v[attr_key] = attr_value
      end
  end
end

-- Specify the file path where you want to save the JSON
local file_path = "JSON//{{TITLE}}.json"

-- Open the file for writing
local file = io.open(file_path, "w")
if file then
    -- Write the JSON directly to the file to avoid large memory usage
    write_json(file, {{FILE_NAME}})
    -- Close the file
    file:close()
    print("JSON data saved to " .. file_path)
else
    print("Error opening file for writing")
end