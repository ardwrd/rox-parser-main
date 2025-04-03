-- Define the JSON serialization function
local function to_json(value)
  if type(value) == "table" then
      local json = "{"
      local first = true
      for k, v in pairs(value) do
          if not first then
              json = json .. ","
          else
              first = false
          end
          json = json .. '"' .. k .. '":' .. to_json(v)
      end
      json = json .. "}"
      return json
  elseif type(value) == "number" or type(value) == "boolean" then
      return tostring(value)
  elseif type(value) == "string" then
      return '"' .. value .. '"'
  else
      return "null"
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

-- Serialize the FILE_NAME table to JSON
local json_string = to_json({{FILE_NAME}})

-- Specify the file path where you want to save the JSON
local file_path = "JSON//{{TITLE}}.json"

-- Open the file for writing
local file = io.open(file_path, "w")
if file then
    -- Write the JSON string to the file
    file:write(json_string)
    -- Close the file
    file:close()
    print("JSON data saved to " .. file_path)
else
    print("Error opening file for writing")
end