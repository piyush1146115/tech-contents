# Supply Chain Security

## Supply Chain Security Benefits

- Early detection of vulnerabilities 
- Better resource management
- Improved compliance
- Efficient incident response
- Enhanced security posture

## Common Threats and Vulnerabilities

- Cyber attacks
- Operational disruptions
- Financial losses
- Regulatory and legal consequences
- Competitive disadvantage

## What is SBOM

- Software bill of materials
- Benefits:
    - Transparency
    - Incident response
    - Dependency management
    - Security
    - Compliance
- Key components
    - Component name
    - Version information
    - Supplier information
    - Licensing information
    - Component dependencies
    - Vulnerability information

## Minimize Base Image Footprint

- Build modular image. Don't build everything in a single base image
- Don't store data inside containers. Always store data in an external volume or caching
- Try to keep the image sizes as small as possible
- Only install neecessary packages
- Find an official minimal image that exists

## SBOM Format

- SBOM CycloneDx format
- SBOM SPDX format
- SPDX is for more standard format
- CycloneDX is lightweight format designed for security and compliance
- SPDX format types are JSON, RDF, Tag/Value
- CycloneDX format types are JSON, XML
- SPDX is more complex due to exteensive metadata coverage
- CycloneDX is simpler and more focusseed on essential SBOM elements

## SBOM - Scan

- `grype` can be used to scan the SBOM reports

## Introduction to Kubelinter
 
 - How Kubelinter works: Configurable checks, Analysis and linting, Repots and suggestions
 - Why use Kubelinter
    - Prevents misconfiguration
    - Improves security
    - Enhances reliability 
    - Enables automated reviews
    - Ensures cost efficiency
    - Helps achieve compliance

## Image Security

- ImagePolicyWebhook can be installed to check the image registries of an image before pulling them to the cluster

## Use static analysis of User workloads

- Static analysis tools analyze the manifest files before deploying to the actual cluster
- One such tool is `kubesec`
- kubesec can be installed locally as a binary or we can use do POST request to hosted kubesec

## Scan images for known vulnerabilities - Trivy

- CVE: Common Vulnerabilities and Exposures
- CVEs have security scores in band 0-10
- Trivy is a simple and comprehensive vulnerability scanner
- `trivy image --severity CRITICAL nginx:1.18.0`
- Best Practices:
    - Continuously rescan images
    - Kubernetes admission controllers to scan images
    - Have your own repository with pre-scanned images ready to go
    - Integrate scanning into your CI/CD pipeline
    