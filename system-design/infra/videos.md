INSERT INTO feature_org_allow_lists 
  (id, feature_id, org_id, description, created_at, updated_at)
VALUES 
  (
    gen_random_uuid(), 
    2,
    'org_4',
    'Allow Orion to Observo org',
    NOW(), 
    NOW()
  );