from config.db_config import get_db_connection

def fetch_claim_data(claim_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM claims WHERE claim_id = %s", (claim_id,))
    result = cursor.fetchone()
    conn.close()
    return result
