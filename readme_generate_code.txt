1. cd swagger-codegen
2. mvn clean package
3. create the stub:

For nexus:

java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate   \
-i ../nexus_swagger.json   \
-l python  \
 -o ../nexus_stub_output_folder \
 -a "Authorization:Basic YWRtaW46NjNhNWZlNjItZThlNi00MWI2LWFmYmMtYWQ3NzU4ZDk1M2Qx"

