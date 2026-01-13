# Blogs

- [I Just want mTLS](https://blog.howardjohn.info/posts/mtls-kubernetes/)
- [Image Management on Kubernetes Node](https://medium.com/@rifewang/image-management-on-kubernetes-node-18649e16bc26)
- [Necessary Culture Change with GitOps](https://itnext.io/necessary-culture-change-with-gitops-2c63f4fe9604)
- [How to Troubleshoot OOM Issues in Go Applications Running on Kubernetes](https://medium.com/@csepulvedab/how-to-troubleshoot-oom-issues-in-go-applications-running-on-kubernetes-149e8bb104ac)
- [Kubernetes 1.33: Resizing Pods Without the Drama (Finally!)](https://itnext.io/kubernetes-1-33-resizing-pods-without-the-drama-finally-88e4791be8d1)
- [Operator Pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
- [Best practices for building Kubernetes Operators and stateful apps](https://cloud.google.com/blog/products/containers-kubernetes/best-practices-for-building-kubernetes-operators-and-stateful-apps)
- [CNCF Operator White Paper - Final Version](https://github.com/cncf/tag-app-delivery/blob/163962c4b1cd70d085107fc579e3e04c2e14d59c/operator-wg/whitepaper/Operator-WhitePaper_v1-0.md#table-of-contents)
    - https://github.com/kubeflow/trainer/issues/300#issuecomment-357527937
- [Optimizing Kubernetes Resource Allocation with Robusta KRR](https://medium.com/hostspaceng/optimizing-kubernetes-resource-allocation-with-robusta-krr-9f08bca2dda2)
- [Load Balancing gRPC traffic with Istio](https://dev.to/visepol/load-balancing-grpc-traffic-with-istio-1k49)
- [Mastering Spot Instances on Kubernetes for Fun and Profit](https://medium.com/@the.gigi/mastering-spot-instances-on-kubernetes-for-fun-and-profit-f274e7d59005)
- [My PodDisruptionBudget bible to use with Karpenter and friends](https://dev.to/aws-builders/my-poddisruptionbudget-bible-to-use-with-karpenter-and-friends-59fl)
- [What's Inside Distroless Container Images: Taking a Closer Look](https://labs.iximiuz.com/tutorials/gcr-distroless-container-images)
- [Docker’s Gone — Here’s Why It’s Time to Move On](https://codingplainenglish.medium.com/docker-is-dead-and-its-about-time-b457d14b0a72)
- [Production-Grade Pain: Lessons From Scaling Kubernetes on EKS](https://engineering.probo.in/production-grade-pain-lessons-from-scaling-kubernetes-on-eks-03571838c7a3)
- [Linux container from scratch](https://michalpitr.substack.com/p/linux-container-from-scratch)
- [The Karpenter Effect: Redefining Our Kubernetes Operations](https://medium.com/learnings-from-the-paas/the-karpenter-effect-redefining-our-kubernetes-operations-80c7ba90a599)
- [Validating Admission Policy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/)

- [Vertical Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/)
    - The VPA consists of three main components:
        - The recommender, which analyzes resource usage and provides recommendations.
        - The updater, that Pod resource requests either by evicting Pods or modifying them in place.
        - And the VPA admission controller webhook, which applies resource recommendations to new or recreated Pods.
    - The Recommender analyzes both current and historical resource usage data (CPU and memory) for each Pod targeted by the VerticalPodAutoscaler. It examines:
        - Historical consumption patterns over time to identify trends
        - Peak usage and variance to ensure sufficient headroom
        - Out-of-memory (OOM) events and other resource-related incidents
    - Based on this analysis, the Recommender calculates three types of recommendations:
        - Target recommendation (optimal resources for typical usage)
        - Lower bound (minimum viable resources)
        - Upper bound (maximum reasonable resources). These recommendations are stored in the VerticalPodAutoscaler resource's .status.recommendation field

- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)

- [1.35 release notes](https://kubernetes.io/blog/2025/12/17/kubernetes-v1-35-release/)

- [Resize CPU and Memory Resources assigned to Containers](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/#pod-resize-status)