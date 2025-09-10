Minimal runbook 

If latest deploy breaks:

ECS → Services → mlops-api-task-service → Deployments → select previous task definition revision → Force new deployment (or aws ecs update-service --task-definition <old-arn>).

If the image is the issue: redeploy last good image tag (you have dual tagging: main + SHA).

Validate health: ALB target is healthy, /health returns 200, error rate returns to baseline.

Postmortem notes: root cause, detection, time to recovery, prevention.

(Later you can automate storing “last good” in SSM and one-click rollbacks.)