# quarkus-offline-dependencies

This application gathers all direct and transitive dependencies used by a Quarkus application (including all POM files) and captures them in a single list. It will also include the `gradle-application-plugin` for Quarkus that matches the same platform version. This assumes you have the `mvn` build tool installed and available on your workstation. It also assumes you have `python` (version 3+) installed and available. 

## Step 1

Generate a sample project at https://code.quarkus.io, selecting the modules you need, and utilizing Maven as the build tool. Download the zip and place it in the `code-with-quarkus` directory of this project, overwriting what is there now.

## Step 2

Adjust the `pom.xml` file to specifically list the desired repositories, and add in the repository for the `gradle-application-plugin`
```
<repositories>
    <repository>
        <id>central</id>
        <name>Central Repository</name>
        <url>https://repo.maven.apache.org/maven2</url>
        <layout>default</layout>
        <snapshots>
            <enabled>false</enabled>
        </snapshots>
    </repository>
    <repository>
        <id>gradlePlugin</id>
        <name>Gradle Plugin Repository</name>
        <url>https://plugins.gradle.org/m2</url>
        <layout>default</layout>
        <snapshots>
            <enabled>false</enabled>
        </snapshots>
    </repository>
</repositories>

<pluginRepositories>
    <pluginRepository>
        <id>central</id>
        <name>Central Repository</name>
        <url>https://repo.maven.apache.org/maven2</url>
        <layout>default</layout>
        <snapshots>
            <enabled>false</enabled>
        </snapshots>
    </pluginRepository>
</pluginRepositories>
```
## Step 3

Add the `gradle-application-plugin` as an explicit dependency in the `pom.xml`, and the Mockito test module, if it wasn't already included:
```
<dependency>
    <groupId>io.quarkus</groupId>
    <artifactId>gradle-application-plugin</artifactId>
    <version>${quarkus.platform.version}</version>
</dependency>   
<dependency>
    <groupId>io.quarkus</groupId>
    <artifactId>quarkus-junit5-mockito</artifactId>
    <scope>test</scope>
</dependency>   
```
## Step 4

Pull the dependencies into a clean local maven repository:
```
make get-dependencies
```
## Step 5

Generate the list of dependencies (shown as relative path within the maven repo):
```
make list-dependencies
```
