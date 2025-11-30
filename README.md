Kubernetes Commands and Their Functions.
Verify Metrics Server
kubectl get pods -n kube-system | grep metrics
Function: Checks that the metrics server is running, which is required for HPA.
Apply Deployment and Service
kubectl apply -f k8s-deployment.yaml
Function: Deploys the OrderAPI application and creates the service in Kubernetes.
Apply Horizontal Pod Autoscaler (HPA)
kubectl apply -f k8s-hpa.yaml
Function: Creates the HPA to automatically scale pods based on CPU usage.
Check HPA Status
kubectl get hpa
Function: Verifies the current scaling metrics and number of replicas.
Check Pods During Load
kubectl get pods
Function: Lists all running pods including the load generator to monitor scaling.
Delete Load Pod
kubectl delete pod load
Function: Removes the load generator pod to test HPA scaling down.
Observe HPA Scaling in Real-Time
kubectl get hpa -w
Function: Watches the HPA adjust the number of replicas dynamically.
Observe Pods After Self-Healing
kubectl get pods
Function: Verifies that pods deleted or failed are automatically replaced.
Perform Rolling Update
kubectl set env deployment/order-api VERSION=v2
kubectl get pods -w
Function: Updates the deployment environment variable to trigger a zero-downtime rolling update and monitors pod creation and termination.
