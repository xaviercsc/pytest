import xml.sax.saxutils as saxutils
 
def create_xml_payload(version, applicationConfig, applicationComponent, attribute, value):
    # Escape special XML characters in the value
    escaped_value = saxutils.escape(value)
 
    # Define the XML template
    xml_template = """<?xml version="1.0" encoding="UTF-8"?>
<registerApplicationComponentVersionAttributeValueRequest>
<applicationConfig>APPLICATIONCONFIG_PLACEHOLDER</applicationConfig>
<applicationComponent>APPLICATIONCOMPONENT_PLACEHOLDER</applicationComponent>
<version>VERSION_PLACEHOLDER</version>
<attribute>ATTRIBUTE_PLACEHOLDER</attribute>
<value>VALUE_PLACEHOLDER</value>
</registerApplicationComponentVersionAttributeValueRequest>"""
 
    # Replace placeholders with actual values
    xml_payload = xml_template.replace('VERSION_PLACEHOLDER', version)
    xml_payload = xml_payload.replace('APPLICATIONCONFIG_PLACEHOLDER', applicationConfig)
    xml_payload = xml_payload.replace('APPLICATIONCOMPONENT_PLACEHOLDER', applicationComponent)
    xml_payload = xml_payload.replace('ATTRIBUTE_PLACEHOLDER', attribute)
    xml_payload = xml_payload.replace('VALUE_PLACEHOLDER', escaped_value)
 
    # Print the XML payload
    print(xml_payload)
 
# Example usage
create_xml_payload(
    version="6607",
    applicationConfig="SCM",
    applicationComponent="CODE",
    attribute="SRC_JMP_SUMMARY",
    value="<![CDATA[PM code build fails when JMP user story has special character & < in it's Text Summary]]>"
)
